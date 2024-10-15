# SNMP MIB module (CTRON-SFPS-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-SFPS-PORT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:29 2024
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

(sfpsPortAttributeAPI,
 sfpsPortAttributeTable,
 sfpsPortConfig,
 sfpsPortStats) = mibBuilder.importSymbols(
    "CTRON-SFPS-INCLUDE-MIB",
    "sfpsPortAttributeAPI",
    "sfpsPortAttributeTable",
    "sfpsPortConfig",
    "sfpsPortStats")

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


# MODULE-IDENTITY


# Types definitions



class SfpsSwitchPort(Integer32):
    """Custom type SfpsSwitchPort based on Integer32"""




class HexInteger(Integer32):
    """Custom type HexInteger based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SfpsInPortConfigTable_Object = MibTable
sfpsInPortConfigTable = _SfpsInPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sfpsInPortConfigTable.setStatus("mandatory")
_SfpsInPortConfigEntry_Object = MibTableRow
sfpsInPortConfigEntry = _SfpsInPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1)
)
sfpsInPortConfigEntry.setIndexNames(
    (0, "CTRON-SFPS-PORT-MIB", "sfpsInPortConfigPort"),
)
if mibBuilder.loadTexts:
    sfpsInPortConfigEntry.setStatus("mandatory")
_SfpsInPortConfigPort_Type = SfpsSwitchPort
_SfpsInPortConfigPort_Object = MibTableColumn
sfpsInPortConfigPort = _SfpsInPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 1),
    _SfpsInPortConfigPort_Type()
)
sfpsInPortConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigPort.setStatus("mandatory")


class _SfpsInPortConfigAdminStatus_Type(Integer32):
    """Custom type sfpsInPortConfigAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("loopback", 4),
          ("other", 1))
    )


_SfpsInPortConfigAdminStatus_Type.__name__ = "Integer32"
_SfpsInPortConfigAdminStatus_Object = MibTableColumn
sfpsInPortConfigAdminStatus = _SfpsInPortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 2),
    _SfpsInPortConfigAdminStatus_Type()
)
sfpsInPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsInPortConfigAdminStatus.setStatus("mandatory")


class _SfpsInPortConfigOperStatus_Type(Integer32):
    """Custom type sfpsInPortConfigOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5),
          ("testing", 7))
    )


_SfpsInPortConfigOperStatus_Type.__name__ = "Integer32"
_SfpsInPortConfigOperStatus_Object = MibTableColumn
sfpsInPortConfigOperStatus = _SfpsInPortConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 3),
    _SfpsInPortConfigOperStatus_Type()
)
sfpsInPortConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigOperStatus.setStatus("mandatory")
_SfpsInPortConfigOperTime_Type = TimeTicks
_SfpsInPortConfigOperTime_Object = MibTableColumn
sfpsInPortConfigOperTime = _SfpsInPortConfigOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 4),
    _SfpsInPortConfigOperTime_Type()
)
sfpsInPortConfigOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigOperTime.setStatus("mandatory")


class _SfpsInPortConfigType_Type(Integer32):
    """Custom type sfpsInPortConfigType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("access-port", 2),
          ("accessOnly", 11),
          ("downlinkFlood", 19),
          ("fclStandby", 14),
          ("flood", 17),
          ("going-to-access", 7),
          ("host-ctl-port", 5),
          ("host-mgmt-port", 4),
          ("hybrid-port", 8),
          ("loopStandby", 15),
          ("network-only", 10),
          ("network-port", 3),
          ("other", 1),
          ("raPrimary", 12),
          ("raStandby", 16),
          ("stand-by", 9),
          ("unknown", 6),
          ("unknown-ra-standby", 20),
          ("uplink", 13),
          ("uplinkFlood", 18))
    )


_SfpsInPortConfigType_Type.__name__ = "Integer32"
_SfpsInPortConfigType_Object = MibTableColumn
sfpsInPortConfigType = _SfpsInPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 5),
    _SfpsInPortConfigType_Type()
)
sfpsInPortConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsInPortConfigType.setStatus("mandatory")
_SfpsInPortConfigReservedBW_Type = Integer32
_SfpsInPortConfigReservedBW_Object = MibTableColumn
sfpsInPortConfigReservedBW = _SfpsInPortConfigReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 6),
    _SfpsInPortConfigReservedBW_Type()
)
sfpsInPortConfigReservedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsInPortConfigReservedBW.setStatus("mandatory")
_SfpsInPortConfigAllocBW_Type = Integer32
_SfpsInPortConfigAllocBW_Object = MibTableColumn
sfpsInPortConfigAllocBW = _SfpsInPortConfigAllocBW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 7),
    _SfpsInPortConfigAllocBW_Type()
)
sfpsInPortConfigAllocBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigAllocBW.setStatus("mandatory")
_SfpsInPortConfigQoS_Type = Integer32
_SfpsInPortConfigQoS_Object = MibTableColumn
sfpsInPortConfigQoS = _SfpsInPortConfigQoS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 8),
    _SfpsInPortConfigQoS_Type()
)
sfpsInPortConfigQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsInPortConfigQoS.setStatus("mandatory")
_SfpsInPortConfigQSize_Type = Integer32
_SfpsInPortConfigQSize_Object = MibTableColumn
sfpsInPortConfigQSize = _SfpsInPortConfigQSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 9),
    _SfpsInPortConfigQSize_Type()
)
sfpsInPortConfigQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigQSize.setStatus("mandatory")
_SfpsInPortConfigQLen_Type = Gauge32
_SfpsInPortConfigQLen_Object = MibTableColumn
sfpsInPortConfigQLen = _SfpsInPortConfigQLen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 10),
    _SfpsInPortConfigQLen_Type()
)
sfpsInPortConfigQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigQLen.setStatus("mandatory")
_SfpsInPortConfigSwitchId_Type = OctetString
_SfpsInPortConfigSwitchId_Object = MibTableColumn
sfpsInPortConfigSwitchId = _SfpsInPortConfigSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 11),
    _SfpsInPortConfigSwitchId_Type()
)
sfpsInPortConfigSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigSwitchId.setStatus("mandatory")


class _SfpsInPortConfigMediaType_Type(Integer32):
    """Custom type sfpsInPortConfigMediaType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("atm-forum-lec", 12),
          ("atm-forum-pvc", 13),
          ("atm-forum-svc", 14),
          ("atm-lec", 3),
          ("atm-pvc", 10),
          ("atm-svc", 9),
          ("ethernet", 1),
          ("fddi", 2),
          ("hcp", 7),
          ("hdp", 8),
          ("inb", 6),
          ("token-ring", 4),
          ("unknown", 11),
          ("wan", 5))
    )


_SfpsInPortConfigMediaType_Type.__name__ = "Integer32"
_SfpsInPortConfigMediaType_Object = MibTableColumn
sfpsInPortConfigMediaType = _SfpsInPortConfigMediaType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 12),
    _SfpsInPortConfigMediaType_Type()
)
sfpsInPortConfigMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigMediaType.setStatus("mandatory")
_SfpsInPortConfigFrontPanelPort_Type = SfpsSwitchPort
_SfpsInPortConfigFrontPanelPort_Object = MibTableColumn
sfpsInPortConfigFrontPanelPort = _SfpsInPortConfigFrontPanelPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 13),
    _SfpsInPortConfigFrontPanelPort_Type()
)
sfpsInPortConfigFrontPanelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigFrontPanelPort.setStatus("mandatory")


class _SfpsInPortConfigLinkStatus_Type(Integer32):
    """Custom type sfpsInPortConfigLinkStatus based on Integer32"""
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
        *(("link-N-A", 4),
          ("linkDown", 3),
          ("linkUp", 2),
          ("other", 1))
    )


_SfpsInPortConfigLinkStatus_Type.__name__ = "Integer32"
_SfpsInPortConfigLinkStatus_Object = MibTableColumn
sfpsInPortConfigLinkStatus = _SfpsInPortConfigLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 14),
    _SfpsInPortConfigLinkStatus_Type()
)
sfpsInPortConfigLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigLinkStatus.setStatus("mandatory")
_SfpsInPortConfigLinkStateAge_Type = TimeTicks
_SfpsInPortConfigLinkStateAge_Object = MibTableColumn
sfpsInPortConfigLinkStateAge = _SfpsInPortConfigLinkStateAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 15),
    _SfpsInPortConfigLinkStateAge_Type()
)
sfpsInPortConfigLinkStateAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigLinkStateAge.setStatus("mandatory")


class _SfpsInPortConfigRouterPort_Type(Integer32):
    """Custom type sfpsInPortConfigRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-router", 3),
          ("other", 1),
          ("router-port", 2))
    )


_SfpsInPortConfigRouterPort_Type.__name__ = "Integer32"
_SfpsInPortConfigRouterPort_Object = MibTableColumn
sfpsInPortConfigRouterPort = _SfpsInPortConfigRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 16),
    _SfpsInPortConfigRouterPort_Type()
)
sfpsInPortConfigRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigRouterPort.setStatus("mandatory")
_SfpsInPortConfigSlotNumber_Type = Integer32
_SfpsInPortConfigSlotNumber_Object = MibTableColumn
sfpsInPortConfigSlotNumber = _SfpsInPortConfigSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 17),
    _SfpsInPortConfigSlotNumber_Type()
)
sfpsInPortConfigSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigSlotNumber.setStatus("mandatory")
_SfpsInPortConfigMib2PortId_Type = Integer32
_SfpsInPortConfigMib2PortId_Object = MibTableColumn
sfpsInPortConfigMib2PortId = _SfpsInPortConfigMib2PortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 18),
    _SfpsInPortConfigMib2PortId_Type()
)
sfpsInPortConfigMib2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigMib2PortId.setStatus("mandatory")
_SfpsInPortConfigTopoAgent_Type = DisplayString
_SfpsInPortConfigTopoAgent_Object = MibTableColumn
sfpsInPortConfigTopoAgent = _SfpsInPortConfigTopoAgent_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 19),
    _SfpsInPortConfigTopoAgent_Type()
)
sfpsInPortConfigTopoAgent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigTopoAgent.setStatus("mandatory")


class _SfpsInPortConfigLayer3Learning_Type(Integer32):
    """Custom type sfpsInPortConfigLayer3Learning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("other", 1))
    )


_SfpsInPortConfigLayer3Learning_Type.__name__ = "Integer32"
_SfpsInPortConfigLayer3Learning_Object = MibTableColumn
sfpsInPortConfigLayer3Learning = _SfpsInPortConfigLayer3Learning_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 1, 1, 22),
    _SfpsInPortConfigLayer3Learning_Type()
)
sfpsInPortConfigLayer3Learning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortConfigLayer3Learning.setStatus("mandatory")
_SfpsOutPortConfigTable_Object = MibTable
sfpsOutPortConfigTable = _SfpsOutPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    sfpsOutPortConfigTable.setStatus("mandatory")
_SfpsOutPortConfigEntry_Object = MibTableRow
sfpsOutPortConfigEntry = _SfpsOutPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1)
)
sfpsOutPortConfigEntry.setIndexNames(
    (0, "CTRON-SFPS-PORT-MIB", "sfpsOutPortConfigPort"),
)
if mibBuilder.loadTexts:
    sfpsOutPortConfigEntry.setStatus("mandatory")
_SfpsOutPortConfigPort_Type = SfpsSwitchPort
_SfpsOutPortConfigPort_Object = MibTableColumn
sfpsOutPortConfigPort = _SfpsOutPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 1),
    _SfpsOutPortConfigPort_Type()
)
sfpsOutPortConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigPort.setStatus("mandatory")


class _SfpsOutPortConfigAdminStatus_Type(Integer32):
    """Custom type sfpsOutPortConfigAdminStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("loopback", 4),
          ("other", 1))
    )


_SfpsOutPortConfigAdminStatus_Type.__name__ = "Integer32"
_SfpsOutPortConfigAdminStatus_Object = MibTableColumn
sfpsOutPortConfigAdminStatus = _SfpsOutPortConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 2),
    _SfpsOutPortConfigAdminStatus_Type()
)
sfpsOutPortConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsOutPortConfigAdminStatus.setStatus("mandatory")


class _SfpsOutPortConfigOperStatus_Type(Integer32):
    """Custom type sfpsOutPortConfigOperStatus based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("invalid-config", 6),
          ("other", 1),
          ("pending-disable", 4),
          ("pending-enable", 5),
          ("testing", 7))
    )


_SfpsOutPortConfigOperStatus_Type.__name__ = "Integer32"
_SfpsOutPortConfigOperStatus_Object = MibTableColumn
sfpsOutPortConfigOperStatus = _SfpsOutPortConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 3),
    _SfpsOutPortConfigOperStatus_Type()
)
sfpsOutPortConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigOperStatus.setStatus("mandatory")
_SfpsOutPortConfigOperTime_Type = TimeTicks
_SfpsOutPortConfigOperTime_Object = MibTableColumn
sfpsOutPortConfigOperTime = _SfpsOutPortConfigOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 4),
    _SfpsOutPortConfigOperTime_Type()
)
sfpsOutPortConfigOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigOperTime.setStatus("mandatory")


class _SfpsOutPortConfigType_Type(Integer32):
    """Custom type sfpsOutPortConfigType based on Integer32"""
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("access-port", 2),
          ("accessOnly", 11),
          ("downlinkFlood", 19),
          ("flood", 17),
          ("going-to-access", 7),
          ("host-ctl-port", 5),
          ("host-mgmt-port", 4),
          ("hybrid-port", 8),
          ("network-only", 10),
          ("network-port", 3),
          ("other", 1),
          ("raPrimary", 12),
          ("stand-by", 9),
          ("standbyFCLConflict", 13),
          ("standbyLoopedPort", 14),
          ("standbyRANonPrimary", 16),
          ("standbyVersionConflict", 15),
          ("unknown", 6),
          ("unknown-ra-standby", 20),
          ("uplinkFlood", 18))
    )


_SfpsOutPortConfigType_Type.__name__ = "Integer32"
_SfpsOutPortConfigType_Object = MibTableColumn
sfpsOutPortConfigType = _SfpsOutPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 5),
    _SfpsOutPortConfigType_Type()
)
sfpsOutPortConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsOutPortConfigType.setStatus("mandatory")
_SfpsOutPortConfigReservedBW_Type = Integer32
_SfpsOutPortConfigReservedBW_Object = MibTableColumn
sfpsOutPortConfigReservedBW = _SfpsOutPortConfigReservedBW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 6),
    _SfpsOutPortConfigReservedBW_Type()
)
sfpsOutPortConfigReservedBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsOutPortConfigReservedBW.setStatus("mandatory")
_SfpsOutPortConfigAllocBW_Type = Integer32
_SfpsOutPortConfigAllocBW_Object = MibTableColumn
sfpsOutPortConfigAllocBW = _SfpsOutPortConfigAllocBW_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 7),
    _SfpsOutPortConfigAllocBW_Type()
)
sfpsOutPortConfigAllocBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigAllocBW.setStatus("mandatory")
_SfpsOutPortConfigQoS_Type = Integer32
_SfpsOutPortConfigQoS_Object = MibTableColumn
sfpsOutPortConfigQoS = _SfpsOutPortConfigQoS_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 8),
    _SfpsOutPortConfigQoS_Type()
)
sfpsOutPortConfigQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsOutPortConfigQoS.setStatus("mandatory")
_SfpsOutPortConfigQSize_Type = Integer32
_SfpsOutPortConfigQSize_Object = MibTableColumn
sfpsOutPortConfigQSize = _SfpsOutPortConfigQSize_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 9),
    _SfpsOutPortConfigQSize_Type()
)
sfpsOutPortConfigQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigQSize.setStatus("mandatory")
_SfpsOutPortConfigQLen_Type = Gauge32
_SfpsOutPortConfigQLen_Object = MibTableColumn
sfpsOutPortConfigQLen = _SfpsOutPortConfigQLen_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 10),
    _SfpsOutPortConfigQLen_Type()
)
sfpsOutPortConfigQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigQLen.setStatus("mandatory")
_SfpsOutPortConfigSwitchId_Type = OctetString
_SfpsOutPortConfigSwitchId_Object = MibTableColumn
sfpsOutPortConfigSwitchId = _SfpsOutPortConfigSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 11),
    _SfpsOutPortConfigSwitchId_Type()
)
sfpsOutPortConfigSwitchId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigSwitchId.setStatus("mandatory")


class _SfpsOutPortConfigMediaType_Type(Integer32):
    """Custom type sfpsOutPortConfigMediaType based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("atm-encap", 9),
          ("atm-forum-lec", 12),
          ("atm-forum-pvc", 13),
          ("atm-forum-svc", 14),
          ("atm-lec", 3),
          ("atm-pvc", 10),
          ("ethernet", 1),
          ("fddi", 2),
          ("hcp", 7),
          ("hdp", 8),
          ("inb", 6),
          ("token-ring", 4),
          ("unknown", 11),
          ("wan", 5))
    )


_SfpsOutPortConfigMediaType_Type.__name__ = "Integer32"
_SfpsOutPortConfigMediaType_Object = MibTableColumn
sfpsOutPortConfigMediaType = _SfpsOutPortConfigMediaType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 12),
    _SfpsOutPortConfigMediaType_Type()
)
sfpsOutPortConfigMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigMediaType.setStatus("mandatory")
_SfpsOutPortConfigFrontPanelPort_Type = SfpsSwitchPort
_SfpsOutPortConfigFrontPanelPort_Object = MibTableColumn
sfpsOutPortConfigFrontPanelPort = _SfpsOutPortConfigFrontPanelPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 13),
    _SfpsOutPortConfigFrontPanelPort_Type()
)
sfpsOutPortConfigFrontPanelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigFrontPanelPort.setStatus("mandatory")


class _SfpsOutPortConfigLinkStatus_Type(Integer32):
    """Custom type sfpsOutPortConfigLinkStatus based on Integer32"""
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
        *(("linkDown", 3),
          ("linkNA", 4),
          ("linkUp", 2),
          ("other", 1))
    )


_SfpsOutPortConfigLinkStatus_Type.__name__ = "Integer32"
_SfpsOutPortConfigLinkStatus_Object = MibTableColumn
sfpsOutPortConfigLinkStatus = _SfpsOutPortConfigLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 14),
    _SfpsOutPortConfigLinkStatus_Type()
)
sfpsOutPortConfigLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigLinkStatus.setStatus("mandatory")
_SfpsOutPortConfigLinkStateAge_Type = TimeTicks
_SfpsOutPortConfigLinkStateAge_Object = MibTableColumn
sfpsOutPortConfigLinkStateAge = _SfpsOutPortConfigLinkStateAge_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 15),
    _SfpsOutPortConfigLinkStateAge_Type()
)
sfpsOutPortConfigLinkStateAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigLinkStateAge.setStatus("mandatory")


class _SfpsOutPortConfigRouterPort_Type(Integer32):
    """Custom type sfpsOutPortConfigRouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-router", 3),
          ("other", 1),
          ("router-port", 2))
    )


_SfpsOutPortConfigRouterPort_Type.__name__ = "Integer32"
_SfpsOutPortConfigRouterPort_Object = MibTableColumn
sfpsOutPortConfigRouterPort = _SfpsOutPortConfigRouterPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 16),
    _SfpsOutPortConfigRouterPort_Type()
)
sfpsOutPortConfigRouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigRouterPort.setStatus("mandatory")
_SfpsOutPortConfigSlotNumber_Type = Integer32
_SfpsOutPortConfigSlotNumber_Object = MibTableColumn
sfpsOutPortConfigSlotNumber = _SfpsOutPortConfigSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 17),
    _SfpsOutPortConfigSlotNumber_Type()
)
sfpsOutPortConfigSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigSlotNumber.setStatus("mandatory")
_SfpsOutPortConfigMib2PortId_Type = Integer32
_SfpsOutPortConfigMib2PortId_Object = MibTableColumn
sfpsOutPortConfigMib2PortId = _SfpsOutPortConfigMib2PortId_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 2, 1, 18),
    _SfpsOutPortConfigMib2PortId_Type()
)
sfpsOutPortConfigMib2PortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortConfigMib2PortId.setStatus("mandatory")
_SfpsPortAttributePort_Type = Integer32
_SfpsPortAttributePort_Object = MibScalar
sfpsPortAttributePort = _SfpsPortAttributePort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 1),
    _SfpsPortAttributePort_Type()
)
sfpsPortAttributePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPortAttributePort.setStatus("mandatory")
_SfpsPortAttributeAttributes_Type = HexInteger
_SfpsPortAttributeAttributes_Object = MibScalar
sfpsPortAttributeAttributes = _SfpsPortAttributeAttributes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 2),
    _SfpsPortAttributeAttributes_Type()
)
sfpsPortAttributeAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPortAttributeAttributes.setStatus("mandatory")


class _SfpsPortAttributeLearnSelfArp_Type(Integer32):
    """Custom type sfpsPortAttributeLearnSelfArp based on Integer32"""
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


_SfpsPortAttributeLearnSelfArp_Type.__name__ = "Integer32"
_SfpsPortAttributeLearnSelfArp_Object = MibScalar
sfpsPortAttributeLearnSelfArp = _SfpsPortAttributeLearnSelfArp_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 1, 3),
    _SfpsPortAttributeLearnSelfArp_Type()
)
sfpsPortAttributeLearnSelfArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsPortAttributeLearnSelfArp.setStatus("mandatory")


class _SfpsPortAttributeAPIVerb_Type(Integer32):
    """Custom type sfpsPortAttributeAPIVerb based on Integer32"""
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
        *(("disablePortAttr", 5),
          ("enablePortAttr", 4),
          ("other", 1),
          ("resetAll", 2),
          ("resetPort", 3))
    )


_SfpsPortAttributeAPIVerb_Type.__name__ = "Integer32"
_SfpsPortAttributeAPIVerb_Object = MibScalar
sfpsPortAttributeAPIVerb = _SfpsPortAttributeAPIVerb_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 1),
    _SfpsPortAttributeAPIVerb_Type()
)
sfpsPortAttributeAPIVerb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPortAttributeAPIVerb.setStatus("mandatory")
_SfpsPortAttributeAPIPort_Type = Integer32
_SfpsPortAttributeAPIPort_Object = MibScalar
sfpsPortAttributeAPIPort = _SfpsPortAttributeAPIPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 2),
    _SfpsPortAttributeAPIPort_Type()
)
sfpsPortAttributeAPIPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPortAttributeAPIPort.setStatus("mandatory")


class _SfpsPortAttributeAPIAttribute_Type(Integer32):
    """Custom type sfpsPortAttributeAPIAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("learnSelfArp", 1),
          ("none", 2))
    )


_SfpsPortAttributeAPIAttribute_Type.__name__ = "Integer32"
_SfpsPortAttributeAPIAttribute_Object = MibScalar
sfpsPortAttributeAPIAttribute = _SfpsPortAttributeAPIAttribute_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 1, 9, 2, 3),
    _SfpsPortAttributeAPIAttribute_Type()
)
sfpsPortAttributeAPIAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsPortAttributeAPIAttribute.setStatus("mandatory")
_SfpsInPortStatsTable_Object = MibTable
sfpsInPortStatsTable = _SfpsInPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sfpsInPortStatsTable.setStatus("mandatory")
_SfpsInPortStatsEntry_Object = MibTableRow
sfpsInPortStatsEntry = _SfpsInPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1)
)
sfpsInPortStatsEntry.setIndexNames(
    (0, "CTRON-SFPS-PORT-MIB", "sfpsInPortStatsPort"),
)
if mibBuilder.loadTexts:
    sfpsInPortStatsEntry.setStatus("mandatory")
_SfpsInPortStatsPort_Type = SfpsSwitchPort
_SfpsInPortStatsPort_Object = MibTableColumn
sfpsInPortStatsPort = _SfpsInPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 1),
    _SfpsInPortStatsPort_Type()
)
sfpsInPortStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsPort.setStatus("mandatory")


class _SfpsInPortStatsAdminStatus_Type(Integer32):
    """Custom type sfpsInPortStatsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsInPortStatsAdminStatus_Type.__name__ = "Integer32"
_SfpsInPortStatsAdminStatus_Object = MibTableColumn
sfpsInPortStatsAdminStatus = _SfpsInPortStatsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 2),
    _SfpsInPortStatsAdminStatus_Type()
)
sfpsInPortStatsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsInPortStatsAdminStatus.setStatus("mandatory")


class _SfpsInPortStatsReset_Type(Integer32):
    """Custom type sfpsInPortStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SfpsInPortStatsReset_Type.__name__ = "Integer32"
_SfpsInPortStatsReset_Object = MibTableColumn
sfpsInPortStatsReset = _SfpsInPortStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 3),
    _SfpsInPortStatsReset_Type()
)
sfpsInPortStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsInPortStatsReset.setStatus("mandatory")
_SfpsInPortStatsOperTime_Type = TimeTicks
_SfpsInPortStatsOperTime_Object = MibTableColumn
sfpsInPortStatsOperTime = _SfpsInPortStatsOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 4),
    _SfpsInPortStatsOperTime_Type()
)
sfpsInPortStatsOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsOperTime.setStatus("mandatory")
_SfpsInPortStatsPkts_Type = Counter32
_SfpsInPortStatsPkts_Object = MibTableColumn
sfpsInPortStatsPkts = _SfpsInPortStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 5),
    _SfpsInPortStatsPkts_Type()
)
sfpsInPortStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsPkts.setStatus("mandatory")
_SfpsInPortStatsDiscardPkts_Type = Counter32
_SfpsInPortStatsDiscardPkts_Object = MibTableColumn
sfpsInPortStatsDiscardPkts = _SfpsInPortStatsDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 6),
    _SfpsInPortStatsDiscardPkts_Type()
)
sfpsInPortStatsDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsDiscardPkts.setStatus("mandatory")
_SfpsInPortStatsBytes_Type = Counter32
_SfpsInPortStatsBytes_Object = MibTableColumn
sfpsInPortStatsBytes = _SfpsInPortStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 7),
    _SfpsInPortStatsBytes_Type()
)
sfpsInPortStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsBytes.setStatus("mandatory")
_SfpsInPortStatsDiscardBytes_Type = Counter32
_SfpsInPortStatsDiscardBytes_Object = MibTableColumn
sfpsInPortStatsDiscardBytes = _SfpsInPortStatsDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 8),
    _SfpsInPortStatsDiscardBytes_Type()
)
sfpsInPortStatsDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsDiscardBytes.setStatus("mandatory")
_SfpsInPortStatsQOverflows_Type = Counter32
_SfpsInPortStatsQOverflows_Object = MibTableColumn
sfpsInPortStatsQOverflows = _SfpsInPortStatsQOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 9),
    _SfpsInPortStatsQOverflows_Type()
)
sfpsInPortStatsQOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsQOverflows.setStatus("mandatory")
_SfpsInPortStatsLinkUps_Type = Counter32
_SfpsInPortStatsLinkUps_Object = MibTableColumn
sfpsInPortStatsLinkUps = _SfpsInPortStatsLinkUps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 10),
    _SfpsInPortStatsLinkUps_Type()
)
sfpsInPortStatsLinkUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsLinkUps.setStatus("mandatory")
_SfpsInPortStatsLinkDowns_Type = Counter32
_SfpsInPortStatsLinkDowns_Object = MibTableColumn
sfpsInPortStatsLinkDowns = _SfpsInPortStatsLinkDowns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 1, 1, 11),
    _SfpsInPortStatsLinkDowns_Type()
)
sfpsInPortStatsLinkDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsInPortStatsLinkDowns.setStatus("mandatory")
_SfpsOutPortStatsTable_Object = MibTable
sfpsOutPortStatsTable = _SfpsOutPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    sfpsOutPortStatsTable.setStatus("mandatory")
_SfpsOutPortStatsEntry_Object = MibTableRow
sfpsOutPortStatsEntry = _SfpsOutPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1)
)
sfpsOutPortStatsEntry.setIndexNames(
    (0, "CTRON-SFPS-PORT-MIB", "sfpsOutPortStatsPort"),
)
if mibBuilder.loadTexts:
    sfpsOutPortStatsEntry.setStatus("mandatory")
_SfpsOutPortStatsPort_Type = SfpsSwitchPort
_SfpsOutPortStatsPort_Object = MibTableColumn
sfpsOutPortStatsPort = _SfpsOutPortStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 1),
    _SfpsOutPortStatsPort_Type()
)
sfpsOutPortStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsPort.setStatus("mandatory")


class _SfpsOutPortStatsAdminStatus_Type(Integer32):
    """Custom type sfpsOutPortStatsAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SfpsOutPortStatsAdminStatus_Type.__name__ = "Integer32"
_SfpsOutPortStatsAdminStatus_Object = MibTableColumn
sfpsOutPortStatsAdminStatus = _SfpsOutPortStatsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 2),
    _SfpsOutPortStatsAdminStatus_Type()
)
sfpsOutPortStatsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsOutPortStatsAdminStatus.setStatus("mandatory")


class _SfpsOutPortStatsReset_Type(Integer32):
    """Custom type sfpsOutPortStatsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2))
    )


_SfpsOutPortStatsReset_Type.__name__ = "Integer32"
_SfpsOutPortStatsReset_Object = MibTableColumn
sfpsOutPortStatsReset = _SfpsOutPortStatsReset_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 3),
    _SfpsOutPortStatsReset_Type()
)
sfpsOutPortStatsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfpsOutPortStatsReset.setStatus("mandatory")
_SfpsOutPortStatsOperTime_Type = TimeTicks
_SfpsOutPortStatsOperTime_Object = MibTableColumn
sfpsOutPortStatsOperTime = _SfpsOutPortStatsOperTime_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 4),
    _SfpsOutPortStatsOperTime_Type()
)
sfpsOutPortStatsOperTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsOperTime.setStatus("mandatory")
_SfpsOutPortStatsPkts_Type = Counter32
_SfpsOutPortStatsPkts_Object = MibTableColumn
sfpsOutPortStatsPkts = _SfpsOutPortStatsPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 5),
    _SfpsOutPortStatsPkts_Type()
)
sfpsOutPortStatsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsPkts.setStatus("mandatory")
_SfpsOutPortStatsDiscardPkts_Type = Counter32
_SfpsOutPortStatsDiscardPkts_Object = MibTableColumn
sfpsOutPortStatsDiscardPkts = _SfpsOutPortStatsDiscardPkts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 6),
    _SfpsOutPortStatsDiscardPkts_Type()
)
sfpsOutPortStatsDiscardPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsDiscardPkts.setStatus("mandatory")
_SfpsOutPortStatsBytes_Type = Counter32
_SfpsOutPortStatsBytes_Object = MibTableColumn
sfpsOutPortStatsBytes = _SfpsOutPortStatsBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 7),
    _SfpsOutPortStatsBytes_Type()
)
sfpsOutPortStatsBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsBytes.setStatus("mandatory")
_SfpsOutPortStatsDiscardBytes_Type = Counter32
_SfpsOutPortStatsDiscardBytes_Object = MibTableColumn
sfpsOutPortStatsDiscardBytes = _SfpsOutPortStatsDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 8),
    _SfpsOutPortStatsDiscardBytes_Type()
)
sfpsOutPortStatsDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsDiscardBytes.setStatus("mandatory")
_SfpsOutPortStatsQOverflows_Type = Counter32
_SfpsOutPortStatsQOverflows_Object = MibTableColumn
sfpsOutPortStatsQOverflows = _SfpsOutPortStatsQOverflows_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 9),
    _SfpsOutPortStatsQOverflows_Type()
)
sfpsOutPortStatsQOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsQOverflows.setStatus("mandatory")
_SfpsOutPortStatsLinkUps_Type = Counter32
_SfpsOutPortStatsLinkUps_Object = MibTableColumn
sfpsOutPortStatsLinkUps = _SfpsOutPortStatsLinkUps_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 10),
    _SfpsOutPortStatsLinkUps_Type()
)
sfpsOutPortStatsLinkUps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsLinkUps.setStatus("mandatory")
_SfpsOutPortStatsLinkDowns_Type = Counter32
_SfpsOutPortStatsLinkDowns_Object = MibTableColumn
sfpsOutPortStatsLinkDowns = _SfpsOutPortStatsLinkDowns_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 2, 4, 2, 1, 2, 2, 2, 1, 11),
    _SfpsOutPortStatsLinkDowns_Type()
)
sfpsOutPortStatsLinkDowns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpsOutPortStatsLinkDowns.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-SFPS-PORT-MIB",
    **{"SfpsSwitchPort": SfpsSwitchPort,
       "HexInteger": HexInteger,
       "sfpsInPortConfigTable": sfpsInPortConfigTable,
       "sfpsInPortConfigEntry": sfpsInPortConfigEntry,
       "sfpsInPortConfigPort": sfpsInPortConfigPort,
       "sfpsInPortConfigAdminStatus": sfpsInPortConfigAdminStatus,
       "sfpsInPortConfigOperStatus": sfpsInPortConfigOperStatus,
       "sfpsInPortConfigOperTime": sfpsInPortConfigOperTime,
       "sfpsInPortConfigType": sfpsInPortConfigType,
       "sfpsInPortConfigReservedBW": sfpsInPortConfigReservedBW,
       "sfpsInPortConfigAllocBW": sfpsInPortConfigAllocBW,
       "sfpsInPortConfigQoS": sfpsInPortConfigQoS,
       "sfpsInPortConfigQSize": sfpsInPortConfigQSize,
       "sfpsInPortConfigQLen": sfpsInPortConfigQLen,
       "sfpsInPortConfigSwitchId": sfpsInPortConfigSwitchId,
       "sfpsInPortConfigMediaType": sfpsInPortConfigMediaType,
       "sfpsInPortConfigFrontPanelPort": sfpsInPortConfigFrontPanelPort,
       "sfpsInPortConfigLinkStatus": sfpsInPortConfigLinkStatus,
       "sfpsInPortConfigLinkStateAge": sfpsInPortConfigLinkStateAge,
       "sfpsInPortConfigRouterPort": sfpsInPortConfigRouterPort,
       "sfpsInPortConfigSlotNumber": sfpsInPortConfigSlotNumber,
       "sfpsInPortConfigMib2PortId": sfpsInPortConfigMib2PortId,
       "sfpsInPortConfigTopoAgent": sfpsInPortConfigTopoAgent,
       "sfpsInPortConfigLayer3Learning": sfpsInPortConfigLayer3Learning,
       "sfpsOutPortConfigTable": sfpsOutPortConfigTable,
       "sfpsOutPortConfigEntry": sfpsOutPortConfigEntry,
       "sfpsOutPortConfigPort": sfpsOutPortConfigPort,
       "sfpsOutPortConfigAdminStatus": sfpsOutPortConfigAdminStatus,
       "sfpsOutPortConfigOperStatus": sfpsOutPortConfigOperStatus,
       "sfpsOutPortConfigOperTime": sfpsOutPortConfigOperTime,
       "sfpsOutPortConfigType": sfpsOutPortConfigType,
       "sfpsOutPortConfigReservedBW": sfpsOutPortConfigReservedBW,
       "sfpsOutPortConfigAllocBW": sfpsOutPortConfigAllocBW,
       "sfpsOutPortConfigQoS": sfpsOutPortConfigQoS,
       "sfpsOutPortConfigQSize": sfpsOutPortConfigQSize,
       "sfpsOutPortConfigQLen": sfpsOutPortConfigQLen,
       "sfpsOutPortConfigSwitchId": sfpsOutPortConfigSwitchId,
       "sfpsOutPortConfigMediaType": sfpsOutPortConfigMediaType,
       "sfpsOutPortConfigFrontPanelPort": sfpsOutPortConfigFrontPanelPort,
       "sfpsOutPortConfigLinkStatus": sfpsOutPortConfigLinkStatus,
       "sfpsOutPortConfigLinkStateAge": sfpsOutPortConfigLinkStateAge,
       "sfpsOutPortConfigRouterPort": sfpsOutPortConfigRouterPort,
       "sfpsOutPortConfigSlotNumber": sfpsOutPortConfigSlotNumber,
       "sfpsOutPortConfigMib2PortId": sfpsOutPortConfigMib2PortId,
       "sfpsPortAttributePort": sfpsPortAttributePort,
       "sfpsPortAttributeAttributes": sfpsPortAttributeAttributes,
       "sfpsPortAttributeLearnSelfArp": sfpsPortAttributeLearnSelfArp,
       "sfpsPortAttributeAPIVerb": sfpsPortAttributeAPIVerb,
       "sfpsPortAttributeAPIPort": sfpsPortAttributeAPIPort,
       "sfpsPortAttributeAPIAttribute": sfpsPortAttributeAPIAttribute,
       "sfpsInPortStatsTable": sfpsInPortStatsTable,
       "sfpsInPortStatsEntry": sfpsInPortStatsEntry,
       "sfpsInPortStatsPort": sfpsInPortStatsPort,
       "sfpsInPortStatsAdminStatus": sfpsInPortStatsAdminStatus,
       "sfpsInPortStatsReset": sfpsInPortStatsReset,
       "sfpsInPortStatsOperTime": sfpsInPortStatsOperTime,
       "sfpsInPortStatsPkts": sfpsInPortStatsPkts,
       "sfpsInPortStatsDiscardPkts": sfpsInPortStatsDiscardPkts,
       "sfpsInPortStatsBytes": sfpsInPortStatsBytes,
       "sfpsInPortStatsDiscardBytes": sfpsInPortStatsDiscardBytes,
       "sfpsInPortStatsQOverflows": sfpsInPortStatsQOverflows,
       "sfpsInPortStatsLinkUps": sfpsInPortStatsLinkUps,
       "sfpsInPortStatsLinkDowns": sfpsInPortStatsLinkDowns,
       "sfpsOutPortStatsTable": sfpsOutPortStatsTable,
       "sfpsOutPortStatsEntry": sfpsOutPortStatsEntry,
       "sfpsOutPortStatsPort": sfpsOutPortStatsPort,
       "sfpsOutPortStatsAdminStatus": sfpsOutPortStatsAdminStatus,
       "sfpsOutPortStatsReset": sfpsOutPortStatsReset,
       "sfpsOutPortStatsOperTime": sfpsOutPortStatsOperTime,
       "sfpsOutPortStatsPkts": sfpsOutPortStatsPkts,
       "sfpsOutPortStatsDiscardPkts": sfpsOutPortStatsDiscardPkts,
       "sfpsOutPortStatsBytes": sfpsOutPortStatsBytes,
       "sfpsOutPortStatsDiscardBytes": sfpsOutPortStatsDiscardBytes,
       "sfpsOutPortStatsQOverflows": sfpsOutPortStatsQOverflows,
       "sfpsOutPortStatsLinkUps": sfpsOutPortStatsLinkUps,
       "sfpsOutPortStatsLinkDowns": sfpsOutPortStatsLinkDowns}
)
